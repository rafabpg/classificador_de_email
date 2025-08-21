import { useState } from "react";
import { FiMail } from "react-icons/fi";
import useUploadFile from "../features/uploadFile/hooks/useFileUpload";
import useUploadText from "../features/textWritting/hooks/useUploadText";
import { Tabs } from "../common/components/Tabs";
import { UploadForm } from "../features/uploadFile/components/UploadFile";
import { TextForm } from "../features/textWritting/components/TextWritting";
import { ResponseDisplay } from "../common/components/ResponseDisplay";
import LoadingPulse from "../common/components/LoadingSpinner";
import type { ResponseAnalysis } from "../common/IResponse";

/**
 * A component to render the home page.
 *
 * It renders a form with a tabbed interface to switch between two modes of data entry:
 * uploading a file or writing text.
 *
 * The component also renders a loading pulse animation when the request is being sent.
 * The component also renders a response display component to show the response from the server.
 *
 * The component uses the useUploadFile and useUploadText hooks to send the request to the server.
 *
 * @returns {React.ReactElement} The home page component.
 */
export const Home = () => {
	const [activeTab, setActiveTab] = useState("upload");
	const [response, setResponse] = useState<ResponseAnalysis | null>(null);

	const { mutate: sendFile, isPulsing: filePulsing } = useUploadFile();
	const { mutate: sendText, isPulsing: textPulsing } = useUploadText();

	const handleFileSubmit = (file: File) => {
		sendFile(file, { onSuccess: setResponse });
	};

	const handleTextSubmit = (text: string) => {
		sendText(text, { onSuccess: setResponse });
	};

	const isLoading = filePulsing || textPulsing;

	return (
		<div className="min-h-screen bg-gradient-to-br from-primary-100/30 to-neutral-100 flex flex-col items-center justify-start py-8 px-4 sm:py-12">
			<div className="w-full max-w-3xl p-6 sm:p-8 bg-surface rounded-2xl shadow-soft border border-neutral-300/50 relative transition-all duration-300 ease-fluid">
				<div className="flex flex-col items-center mb-6">
					<div className="p-3 bg-primary-100 rounded-full mb-4">
						<FiMail className="h-8 w-8 text-primary-700" />
					</div>
					<h1 className="text-2xl sm:text-3xl font-bold text-primary-700 text-center font-display">
						Classificador de Emails
					</h1>
					<p className="text-neutral-600 mt-2 text-center max-w-md">
						Automatize a análise de seus emails com IA
					</p>
				</div>

				<Tabs activeTab={activeTab} setActiveTab={setActiveTab} />

				<div className="mt-4">
					{activeTab === "upload" && (
						<UploadForm onSubmit={handleFileSubmit} isLoading={filePulsing} />
					)}

					{activeTab === "text" && (
						<TextForm onSubmit={handleTextSubmit} isLoading={textPulsing} />
					)}
				</div>
				<div className="mt-8">
					<LoadingPulse isVisible={isLoading} />

					<ResponseDisplay
						response={response}
						onClear={() => setResponse(null)}
					/>
				</div>

				<div className="absolute -top-2 -right-2 h-16 w-16 bg-accent-400/10 rounded-full -z-10"></div>
				<div className="absolute -bottom-2 -left-2 h-20 w-20 bg-primary-500/5 rounded-full -z-10"></div>
			</div>

			<div className="mt-8 text-center text-xs text-neutral-500 max-w-2xl">
				<p className="mb-2">
					Utilize esta ferramenta para classificar automaticamente os conteúdos
					dos seus emails em categorias como "Produtivo" ou "Improdutivo"
				</p>
				<p>Suporte a arquivos .txt, .pdf e texto digitado</p>
			</div>
		</div>
	);
};
