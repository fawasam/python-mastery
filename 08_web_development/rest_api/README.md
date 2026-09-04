# REST API Architecture in Python

## What You Will Learn
* REST (Representational State Transfer) architectural constraints.
* Naming API Resources & Collections (plural nouns: `/users`, `/orders/{id}`).
* Standard HTTP verb mappings:
  - `GET`: Read resource (Idempotent).
  - `POST`: Create new resource.
  - `PUT`: Replace entire resource.
  - `PATCH`: Partially update resource.
  - `DELETE`: Remove resource.
* Standard JSON API responses and HTTP status code mappings.

## Why This Matters
REST APIs are the ubiquitous industry standard for web services, mobile backends, and microservice integration. Designing clear, predictable API resource endpoints makes APIs intuitive and easy to consume.

## Prerequisites
* HTTP & Requests (`08_web_development/http`, `08_web_development/requests`)

## Core Concepts

### REST Endpoint Mapping Table
| Verb | Path | Action | Success Code |
|---|---|---|---|
| GET | `/items` | List all items | 200 OK |
| POST | `/items` | Create new item | 201 Created |
| GET | `/items/{id}` | Retrieve specific item | 200 OK |
| PUT | `/items/{id}` | Replace item | 200 OK |
| DELETE | `/items/{id}` | Delete item | 204 No Content |

## Exercises
See `04_exercises.py` to practice constructing RESTful route handlers.
