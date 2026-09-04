# HTTP Fundamentals in Python

## What You Will Learn
* The Client-Server HTTP architecture.
* HTTP Request Anatomy (Method, URI, Headers, Query Parameters, Body).
* HTTP Response Status Codes (2xx Success, 3xx Redirect, 4xx Client Error, 5xx Server Error).
* MIME Content Types (`application/json`, `text/html`, `multipart/form-data`).

## Why This Matters
Web applications, REST APIs, and microservices exchange data over HTTP (Hypertext Transfer Protocol). Understanding status codes, headers, and payload formatting is mandatory for constructing and consuming web services.

## Prerequisites
* Basic JSON Parsing (`02_core_python/json`)

## Core Concepts

### HTTP Status Code Ranges
- **200 OK / 201 Created**: Request succeeded.
- **400 Bad Request**: Client sent invalid syntax or payload.
- **401 Unauthorized**: Authentication credentials missing/invalid.
- **403 Forbidden**: Client lacks permission for resource.
- **404 Not Found**: Resource URI does not exist.
- **500 Internal Server Error**: Server encountered unhandled exception.

## Exercises
See `04_exercises.py` to practice parsing HTTP response codes and headers.
