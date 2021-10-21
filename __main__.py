"""A Google Cloud Python Pulumi program"""

import pulumi
import pulumi_gcp as gcp

#Enable API Services

project = gcp.projects.Service("workflow_api",
    disable_dependent_services=True,
    project="plucky-operand-321715",
    service="workflows.googleapis.com")

project = gcp.projects.Service("cloudfunctions_api",
    disable_dependent_services=True,
    project="plucky-operand-321715",
    service="cloudfunctions.googleapis.com")

project = gcp.projects.Service("cloudresourcemanager_api",
    disable_dependent_services=True,
    project="plucky-operand-321715",
    service="cloudresourcemanager.googleapis.com")

project = gcp.projects.Service("containerregistry_api",
    disable_dependent_services=True,
    project="plucky-operand-321715",
    service="containerregistry.googleapis.com")

project = gcp.projects.Service("datafusion_api",
    disable_dependent_services=True,
    project="plucky-operand-321715",
    service="datafusion.googleapis.com")

project = gcp.projects.Service("monitoring_api",
    disable_dependent_services=True,
    project="plucky-operand-321715",
    service="monitoring.googleapis.com")

project = gcp.projects.Service("secretmanager_api",
    disable_dependent_services=True,
    project="plucky-operand-321715",
    service="secretmanager.googleapis.com")

project = gcp.projects.Service("cloudscheduler_api",
    disable_dependent_services=True,
    project="plucky-operand-321715",
    service="cloudscheduler.googleapis.com")

project = gcp.projects.Service("storage_component_api",
    disable_dependent_services=True,
    project="plucky-operand-321715",
    service="storage-component.googleapis.com")

project = gcp.projects.Service("pubsub_api",
    disable_dependent_services=True,
    project="plucky-operand-321715",
    service="pubsub.googleapis.com")

project = gcp.projects.Service("bigquery_api",
    disable_dependent_services=True,
    project="plucky-operand-321715",
    service="bigquery.googleapis.com")

project = gcp.projects.Service("bigquerystorage_api",
    disable_dependent_services=True,
    project="plucky-operand-321715",
    service="bigquerystorage.googleapis.com")

project = gcp.projects.Service("bigtableadmin_api",
    disable_dependent_services=True,
    project="plucky-operand-321715",
    service="bigtableadmin.googleapis.com")

project = gcp.projects.Service("bigqueryconnection_api",
    disable_dependent_services=True,
    project="plucky-operand-321715",
    service="bigqueryconnection.googleapis.com")

project = gcp.projects.Service("firestore_api",
    disable_dependent_services=True,
    project="plucky-operand-321715",
    service="firestore.googleapis.com")

project = gcp.projects.Service("datacatalog_api",
    disable_dependent_services=True,
    project="plucky-operand-321715",
    service="datacatalog.googleapis.com")

project = gcp.projects.Service("cloudlatencytest_api",
    disable_dependent_services=True,
    project="plucky-operand-321715",
    service="cloudlatencytest.googleapis.com")


project = gcp.projects.Service("composer_api",
    disable_dependent_services=True,
    project="plucky-operand-321715",
    service="composer.googleapis.com")


project = gcp.projects.Service("iam_api",
    disable_dependent_services=True,
    project="plucky-operand-321715",
    service="iam.googleapis.com")

project = gcp.projects.Service("aiplatform_api",
    disable_dependent_services=True,
    project="plucky-operand-321715",
    service="aiplatform.googleapis.com")

project = gcp.projects.Service("dlp_api",
    disable_dependent_services=True,
    project="plucky-operand-321715",
    service="dlp.googleapis.com")

#Service account 
import pulumi
import pulumi_gcp as gcp

service_account = gcp.serviceaccount.Account("SegmentSA",
    account_id="uvn-ott-pro-segment",
    display_name="segment service account")

    