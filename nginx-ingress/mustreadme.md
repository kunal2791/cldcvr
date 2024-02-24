helm upgrade -i nginx-ingress ingress-nginx/ingress-nginx --namespace default
kubectl apply -f test.yaml

kubectl apply -f argocd/argocd.yaml -n argocd 
kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'