"""
Basic REST API Routing and In-Memory CRUD Handler Simulation.
"""

from typing import Any


class InMemoryRESTController:
    """
    In-memory simulation of a RESTful Controller for /items resource.
    """

    def __init__(self) -> None:
        self._db: dict[int, dict[str, Any]] = {}
        self._next_id = 1

    def handle_request(self, method: str, path: str, payload: dict[str, Any] | None = None) -> tuple[int, Any]:
        parts = [p for p in path.strip("/").split("/") if p]

        # GET /items -> List Collection
        if method == "GET" and parts == ["items"]:
            return 200, list(self._db.values())

        # POST /items -> Create Resource
        if method == "POST" and parts == ["items"]:
            if not payload or "name" not in payload:
                return 400, {"error": "Missing 'name' field"}
            item_id = self._next_id
            self._next_id += 1
            record = {"id": item_id, "name": payload["name"]}
            self._db[item_id] = record
            return 201, record

        # GET /items/{id} -> Single Resource
        if method == "GET" and len(parts) == 2 and parts[0] == "items":
            item_id = int(parts[1])
            if item_id not in self._db:
                return 404, {"error": "Item not found"}
            return 200, self._db[item_id]

        return 405, {"error": "Method Not Allowed"}


if __name__ == "__main__":
    controller = InMemoryRESTController()

    status, created = controller.handle_request("POST", "/items", {"name": "Keyboard"})
    print(f"POST /items -> Status {status}: {created}")

    status, item = controller.handle_request("GET", f"/items/{created['id']}")
    print(f"GET /items/{created['id']} -> Status {status}: {item}")
