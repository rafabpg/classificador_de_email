import { useMutation } from "@tanstack/react-query";
import { apiFiles } from "../../../common/api_files";
import { useNotification } from "../../../common/hooks/useNotification";
import usePulse from "../../../common/hooks/usePulse";
import { queryClient } from "../../../config/queryClient";

/**
 * Hook to send a text to be analyzed.
 *
 * It uses the apiFiles hook to upload the text to the server.
 * The hook also uses the useNotification hook to show a notification when the request is sent.
 * The hook also uses the usePulse hook to show a pulsing animation when the request is sent.
 *
 * It returns an object with the properties:
 * - isPulsing: A boolean indicating whether the pulsing animation is active.
 * - mutate: A function to send the request. It takes a string as argument, which is the text to be sent.
 * - isLoading: A boolean indicating whether the request is being sent.
 * - isError: A boolean indicating whether the request has failed.
 * - isSuccess: A boolean indicating whether the request has succeeded.
 * - error: An object with the error message, if the request has failed.
 * - data: The response from the server, if the request has succeeded.
 *
 * @returns {Object} An object with the properties mentioned above.
 */
const useUploadText = () => {
	const { uploadText } = apiFiles();
	const { showSuccess, showError } = useNotification();
	const { isPulsing, startPulse, stopPulse } = usePulse();

	const mutation = useMutation({
		mutationFn: async (text: string) => {
			return await uploadText(text);
		},
		onMutate: () => startPulse(),
		onSuccess: () => {
			stopPulse();
			queryClient.invalidateQueries({ queryKey: ["analysis"] });
			showSuccess("Texto enviado com sucesso!");
		},
		onError: (error: any) => {
			stopPulse();
			showError(`Erro ao enviar arquivo: ${error?.response?.data?.detail}`);
		},
	});

	return { ...mutation, isPulsing };
};

export default useUploadText;
