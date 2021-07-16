import pulumi
import pulumi_kubernetes as kubernetes

_mysql_pod__pod = kubernetes.core.v1.Pod("mysql_pod",
    api_version="v1",
    kind="Pod",
    metadata=kubernetes.meta.v1.ObjectMetaArgs(
        name="mysql-pod",
        labels={
            "run": "mysql",
        },
    ),
    spec=kubernetes.core.v1.PodSpecArgs(
        containers=[kubernetes.core.v1.ContainerArgs(
            name="mysql-c1",
            image="mysql:5.7",
            env=[
                kubernetes.core.v1.EnvVarArgs(
                    name="MYSQL_ROOT_PASSWORD",
                    value_from={
                        "secret_key_ref": {
                            "name": "dbsecret",
                            "key": "r",
                        },
                    },
                ),
                kubernetes.core.v1.EnvVarArgs(
                    name="MYSQL_DATABASE",
                    value_from={
                        "secret_key_ref": {
                            "name": "dbsecret",
                            "key": "d",
                        },
                    },
                ),
                kubernetes.core.v1.EnvVarArgs(
                    name="MYSQL_USER",
                    value_from={
                        "secret_key_ref": {
                            "name": "dbsecret",
                            "key": "u",
                        },
                    },
                ),
                kubernetes.core.v1.EnvVarArgs(
                    name="MYSQL_PASSWORD",
                    value_from={
                        "secret_key_ref": {
                            "name": "dbsecret",
                            "key": "p",
                        },
                    },
                ),
            ],
        )],
    ))
_dbsecret__secret = kubernetes.core.v1.Secret("dbsecret",
    api_version="v1",
    kind="Secret",
    metadata=kubernetes.meta.v1.ObjectMetaArgs(
        name="dbsecret",
    ),
    data={
        "r": "ZGltcHUxMjM0NQ==",
        "p": "YWplZXQxMjM0NQ==",
        "u": "YWplZXQ=",
        "d": "d29yZHByZXNzX2Ri",
    })
_mysql_svc__service = kubernetes.core.v1.Service("mysql_svc",
    api_version="v1",
    kind="Service",
    metadata=kubernetes.meta.v1.ObjectMetaArgs(
        name="mysql-svc",
    ),
    spec=kubernetes.core.v1.ServiceSpecArgs(
        selector={
            "run": "mysql",
        },
        ports=[kubernetes.core.v1.ServicePortArgs(
            port=3306,
        )],
        cluster_ip="None",
    ))
_wordpress_svc__service = kubernetes.core.v1.Service("wordpress_svc",
    api_version="v1",
    kind="Service",
    metadata=kubernetes.meta.v1.ObjectMetaArgs(
        name="wordpress-svc",
    ),
    spec=kubernetes.core.v1.ServiceSpecArgs(
        selector={
            "run": "wordpress",
        },
        ports=[kubernetes.core.v1.ServicePortArgs(
            protocol="TCP",
            port=80,
            node_port=30002,
        )],
        type="NodePort",
    ))
_wordpress_pod__pod = kubernetes.core.v1.Pod("wordpress_pod",
    api_version="v1",
    kind="Pod",
    metadata=kubernetes.meta.v1.ObjectMetaArgs(
        name="wordpress-pod",
        labels={
            "run": "wordpress",
        },
    ),
    spec=kubernetes.core.v1.PodSpecArgs(
        containers=[kubernetes.core.v1.ContainerArgs(
            name="wp-c1",
            image="wordpress:5.1.1-php7.3-apache",
            env=[
                kubernetes.core.v1.EnvVarArgs(
                    name="WORDPRESS_DB_HOST",
                    value="mysql-svc",
                ),
                kubernetes.core.v1.EnvVarArgs(
                    name="WORDPRESS_DB_USER",
                    value_from={
                        "secret_key_ref": {
                            "name": "dbsecret",
                            "key": "u",
                        },
                    },
                ),
                kubernetes.core.v1.EnvVarArgs(
                    name="WORDPRESS_DB_PASSWORD",
                    value_from={
                        "secret_key_ref": {
                            "name": "dbsecret",
                            "key": "p",
                        },
                    },
                ),
                kubernetes.core.v1.EnvVarArgs(
                    name="WORDPRESS_DB_NAME",
                    value_from={
                        "secret_key_ref": {
                            "name": "dbsecret",
                            "key": "d",
                        },
                    },
                ),
            ],
        )],
    ))
