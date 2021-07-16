# PULUMI-K8S-wordpress
This Repository used to deploy a WordPress site and a MySQL database in K8s Cluster (Minikube),\
using *Pulumi*

**WordPress**, it is the simplest, most popular way to create your own website or blog.\
**MySQL**, free and open source widely used relational database management system (RDBMS).\
**Minikube** is local Single-Node Kubernetes Cluster, focusing on making it easy to learn and develop for Kubernetes.

***Pulumi.yaml*** : that file define the project\
***__main.py__*** : is the Pulumi (Python) Program file, that contains/define stack resources.


`kubectl config set-context pulumi-context --cluster=pulumi-cluster --user=pulumi-user`\
The kubeconfig file defines some number of contexts.\
Each context is a name that is associated with a cluster, namespace, and a “user” (a local-only name that’s associated with a credential that allows access to the cluster).

`pulumi config set kubernetes:context pulumi-context`\
set context (pulumi-context)

`pulumi new kubernetes-python`
   - project name
   - project description
   - stack name : (dev)

`pulumi up`\
Create or Update the Resource's
