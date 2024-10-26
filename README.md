# Valkyria

A discord bot to settle conflicts between friend regarding which coffee shop to visit during weekends.

## Deployment

Valkyria, being a stateful application, is hosted as a single replica on Kubernetes with a Recreate deployment strategy. 
Browse [deployment.yaml](kustomize/deployment.yaml) for details. A `secret` is required to be loaded into the system
separately from the deployment files that is expected to contain the bot key. The secret is expected to be named `valkyria-bot-key` 
and contain a key named `token` which contains the discord bot key. It can be created like so:

`kubectl -n <namespace> create secret generic valkyria-bot-key --from-literal=token=<bot key>`

When updating the version we want to run, we pre-emptively update [deployment.yaml](kustomize/deployment.yaml) with the new image version, like
`image: ghcr.io/OlofHaglund/Valkyria:v0.0.1` would turn into `image: ghcr.io/OlofHaglund/Valkyria:v0.0.2`. Once this is merged, the repository
is tagged and the build will create a container image that is tagged accordingly.
