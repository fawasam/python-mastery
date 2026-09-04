"""
Basic Role-Based Access Control (RBAC) Pattern.
"""

from enum import Enum


class Role(str, Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    VIEWER = "viewer"


ROLE_HIERARCHY = {
    Role.ADMIN: {Role.ADMIN, Role.EDITOR, Role.VIEWER},
    Role.EDITOR: {Role.EDITOR, Role.VIEWER},
    Role.VIEWER: {Role.VIEWER},
}


def is_authorized(user_role: Role, required_permission: Role) -> bool:
    allowed_roles = ROLE_HIERARCHY.get(user_role, set())
    return required_permission in allowed_roles


if __name__ == "__main__":
    assert is_authorized(Role.ADMIN, Role.EDITOR) is True
    assert is_authorized(Role.VIEWER, Role.ADMIN) is False
    assert is_authorized(Role.EDITOR, Role.VIEWER) is True
    print("RBAC role hierarchy authorization checks passed successfully!")
