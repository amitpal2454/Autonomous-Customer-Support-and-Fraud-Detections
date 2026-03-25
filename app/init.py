import os

structure = {
    "app": [
        "main.py",
        "dependencies.py",
        "routes/chat.py",
        "routes/websocket.py",
        "routes/review.py",
        "routes/session.py",
        "routes/webhook.py",
        "routes/health.py",
    ],
    "agents": [
        "supervisor.py",
        "support_agent.py",
        "retention_agent.py",
        "fraud_agent.py",
    ],
    "graph": [
        "workflow.py",
        "nodes.py",
        "edges.py",
        "prompts.py",
    ],
    "tools": [
        "shopify.py",
        "stripe.py",
        "refund_api.py",
        "offer_engine.py",
        "rag.py",
        "azure_ml.py",
        "fraud_protection.py",
        "redis_store.py",
        "comms.py",
        "crm.py",
    ],
    "models": [
        "enums.py",
        "schema.py",
        "api_models.py",
        "cosmos_models.py",
        "validators.py",
    ],
    "memory": [
        "connection.py",
        "checkpoint.py",
        "customers.py",
        "sessions.py",
        "fraud_audit.py",
    ],
    "data/raw": [
        "return_policy.md",
        "faq.md",
        "sample_customers.json",
        "sample_orders.json",
    ],
    "data/processed": [
        "chunks.json",
        "index_schema.json",
        "seed_script.py",
    ],
    "utils": [
        "logger.py",
        "config.py",
        "auth.py",
        "serialiser.py",
    ],
    "infra/docker": [
        "Dockerfile",
        "docker-compose.yml",
        ".dockerignore",
    ],
    "infra/ci_cd": [
        "deploy.yml",
        "pr_checks.yml",
    ],
    "infra/bicep": [
        "main.bicep",
        "cosmos.bicep",
        "container_app.bicep",
        "ai_search.bicep",
        "redis.bicep",
        "keyvault.bicep",
        "openai.bicep",
        "ml.bicep",
    ],
    "tests/unit": [
        "test_models.py",
        "test_fraud_rules.py",
        "test_offer_engine.py",
        "test_validators.py",
        "test_serialiser.py",
    ],
    "tests/integration": [
        "test_support_agent.py",
        "test_retention_agent.py",
        "test_fraud_agent.py",
        "test_supervisor.py",
        "test_cosmos.py",
    ],
    "config": [
        "development.yaml",
        "production.yaml",
        "test.yaml",
        "fraud_rules.yaml",
        "offer_rules.yaml",
    ],
}

def create_structure(base_path="."):
    for folder, files in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)

        for file in files:
            file_path = os.path.join(folder_path, file)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    f.write("# Auto-generated\n")

    print("✅ Project structure created successfully!")

if __name__ == "__main__":
    create_structure()