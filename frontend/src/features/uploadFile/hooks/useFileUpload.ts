import { useMutation } from "@tanstack/react-query";
import { apiFiles } from "../../../common/api_files";
import { queryClient } from "../../../config/queryClient";
import { useNotification } from "../../../common/hooks/useNotification";
import usePulse from "../../../common/hooks/usePulse";

const useUploadFile = () => {
  const { uploadFile } = apiFiles();
  const { showSuccess, showError } = useNotification();
  const { isPulsing, startPulse, stopPulse } = usePulse();

  const mutation = useMutation({
    mutationFn: async (file: File) => {
      return await uploadFile(file);
    },
    onMutate: () => startPulse(),
    onSuccess: () => {
      stopPulse();
      queryClient.invalidateQueries({ queryKey: ["analysis"] });
      showSuccess("Arquivo enviado com sucesso!");
    },
    onError: (error: any) => {
      stopPulse();
      showError(`Erro ao enviar arquivo: ${error?.response?.data?.detail}`);
    },
  });

  return { ...mutation, isPulsing };
};

export default useUploadFile;
