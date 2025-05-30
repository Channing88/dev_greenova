# Stub file for core.templatetags.core_tags
from typing import Any

from django.template import Library

register: Library

def active_link(context: Any, url_name: str, css_class: str = ...) -> str: ...
def breadcrumb_navigation(context: Any) -> dict: ...
def auth_menu(context: Any) -> dict: ...
def theme_switcher() -> dict: ...
def site_version() -> str: ...
def main_navigation(context: Any) -> dict: ...
def user_role_in_project(project: Any, user: Any) -> Any: ...
def base_url(context: Any) -> str: ...
