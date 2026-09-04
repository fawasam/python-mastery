"""
Common Mistakes in API Documentation.
"""


# MISTAKE 1: Omitting field descriptions or return type annotations in public API routes
def mistake_undocumented_endpoint() -> None:
    # DANGER: Writing routes with `dict` return annotations and no Pydantic response models
    # causes auto-generated OpenAPI documentation to omit schema structures!
    pass


if __name__ == "__main__":
    print("Always use explicit Pydantic response_model schemas and Field(description=...) annotations!")
