import { useMutation } from "@tanstack/react-query";
import { apiFiles } from "../../../common/api_files";
import { useNotification } from "../../../common/hooks/useNotification";
import usePulse from "../../../common/hooks/usePulse";
import { queryClient } from "../../../config/queryClient";

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
