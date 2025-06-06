import logging

import matplotlib
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from django.views.decorators.vary import vary_on_headers
from django.views.generic import ListView, TemplateView
from projects.models import Project

from .figures import get_mechanism_chart, get_overall_chart
from .models import EnvironmentalMechanism

matplotlib.use("Agg")  # Use Agg backend for non-interactive plotting

logger = logging.getLogger(__name__)


@method_decorator(cache_control(max_age=300), name="dispatch")
@method_decorator(vary_on_headers("HX-Request"), name="dispatch")
class MechanismChartView(LoginRequiredMixin, TemplateView):
    template_name = "mechanisms/mechanism_charts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_id = self.request.GET.get("project_id")

        if not project_id:
            context["error"] = "No project selected"
            return context

        try:
            project_id = int(project_id)
            if project_id < 1:
                context["error"] = "No project selected"
                return context
        except (TypeError, ValueError):
            context["error"] = "Invalid project ID"
            return context

        try:
            # Check if project exists
            project = Project.objects.get(id=project_id)

            # Get mechanisms for this project
            mechanisms = EnvironmentalMechanism.objects.filter(project_id=project_id)

            # Generate charts for each mechanism
            mechanism_charts = []

            # Add overall chart first
            _, overall_chart_data = get_overall_chart(project_id)

            mechanism_charts.append(
                {"name": "Overall Status", "image_data": overall_chart_data}
            )

            # Generate charts for individual mechanisms
            for mechanism in mechanisms:
                _, chart_data = get_mechanism_chart(mechanism.id)

                mechanism_charts.append(
                    {
                        "id": mechanism.id,
                        "name": mechanism.name,
                        "image_data": chart_data,
                    }
                )

            context["mechanism_charts"] = mechanism_charts
            context["project"] = project

            # Add table data with mechanism ID
            context["table_data"] = [
                {
                    "id": m.id,
                    "name": m.name,
                    "not_started": m.not_started_count,
                    "in_progress": m.in_progress_count,
                    "completed": m.completed_count,
                    "overdue": m.overdue_count,
                    "total": (
                        m.not_started_count
                        + m.in_progress_count
                        + m.completed_count
                        + m.overdue_count
                    ),
                }
                for m in mechanisms
            ]

        except Project.DoesNotExist:
            context["error"] = f"Project with ID {project_id} not found"
        except Project.DoesNotExist:
            context["error"] = f"Project with ID {project_id} not found"
        except EnvironmentalMechanism.DoesNotExist:
            context["error"] = "No mechanisms found for the selected project"
        except ValueError as e:
            logger.error("Value error while generating mechanism charts: %s", str(e))
            context["error"] = f"Invalid data encountered: {e!s}"
        except RuntimeError as e:
            logger.error("Runtime error generating mechanism charts: %s", str(e))
            context["error"] = "A runtime error occurred. Please try again later."

        return context


class MechanismListView(LoginRequiredMixin, ListView):
    """List all environmental mechanisms."""

    model = EnvironmentalMechanism
    template_name = "mechanisms/mechanisms_list.html"
    context_object_name = "mechanisms"

    def get_queryset(self):
        return EnvironmentalMechanism.objects.all()
