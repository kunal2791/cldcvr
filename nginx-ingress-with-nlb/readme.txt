helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx

helm install nginx-ingress ingress-nginx/ingress-nginx --set-string controller.service.externalTrafficPolicy=Local --set-string controller.service.type=NodePort --set controller.publishService.enabled=true --set serviceAccount.create=true --set rbac.create=true --set-string controller.config.server-tokens=false --set-string controller.config.use-proxy-protocol=false --set-string controller.config.compute-full-forwarded-for=true --set-string controller.config.use-forwarded-headers=true --set controller.metrics.enabled=true --set controller.autoscaling.maxReplicas=1 --set controller.autoscaling.minReplicas=1 --set controller.autoscaling.enabled=true --namespace kube-system -f nginx-values.yaml

kubectl apply -f alb.yaml