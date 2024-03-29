/*
Copyright 2019 The Kubernetes Authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

package ssh

import (
	"github.com/spf13/cobra"

	"k8s.io/cli-runtime/pkg/genericclioptions"

	"k8s.io/ingress-nginx/cmd/plugin/kubectl"
	"k8s.io/ingress-nginx/cmd/plugin/request"
	"k8s.io/ingress-nginx/cmd/plugin/util"
)

// CreateCommand creates and returns this cobra subcommand
func CreateCommand(flags *genericclioptions.ConfigFlags) *cobra.Command {
	var pod, deployment, selector, container *string
	cmd := &cobra.Command{
		Use:   "ssh",
		Short: "ssh into a running ingress-nginx pod",
		RunE: func(_ *cobra.Command, _ []string) error {
			util.PrintError(ssh(flags, *pod, *deployment, *selector, *container))
			return nil
		},
	}
	pod = util.AddPodFlag(cmd)
	deployment = util.AddDeploymentFlag(cmd)
	selector = util.AddSelectorFlag(cmd)
	container = util.AddContainerFlag(cmd)

	return cmd
}

func ssh(flags *genericclioptions.ConfigFlags, podName, deployment, selector, container string) error {
	pod, err := request.ChoosePod(flags, podName, deployment, selector)
	if err != nil {
		return err
	}

	return kubectl.Exec(flags, []string{"exec", "-it", "-n", pod.Namespace, "-c", container, pod.Name, "--", "/bin/bash"})
}
