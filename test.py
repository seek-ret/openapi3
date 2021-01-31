import json
import openapi3

with open("/home/guy/code/MultiFuzz/playbooks/workflows.json", "r") as f:
    workflows = json.load(f)


openapi_root = openapi3.OpenAPI({
    "paths": {},
    "info": {
        "contact": {
            "email": "info@seekret.com",
            "url": "https://www.seekret.com"
        },
        "description": "This OpenAPI3 file was automatically generated using Seekret Application©",
        "license": {
            "name": "Apache 2.0"
        },
        "title": "Auto-generated OpenAPI3",
        "version": "1.0.0"
    },
    "openapi": "3.0.0",
})

new_workflows = []

for workflow in workflows:
    current_workflow = []
    for elem in workflow:
        endpoint = elem["Endpoint"]
        endpoint_path = endpoint["path"]
        endpoint_method = endpoint["method"].lower()
        operation = elem["Operation"]
        current_workflow.append(openapi3.paths.Operation(["paths", endpoint_path, endpoint_method], operation, openapi_root))
    new_workflows.append(current_workflow)

print(new_workflows)