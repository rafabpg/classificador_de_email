import { useState, useRef, useCallback } from "react";
import { FiUpload, FiX, FiFile, FiSend } from "react-icons/fi";

interface UploadFormProps {
	onSubmit: (file: File) => void;
	isLoading: boolean;
}

/**
 * A component to render a file upload form.
 *
 * Props:
 * - `onSubmit`: A callback to be called when the form is submitted.
 * - `isLoading`: A boolean indicating if the form is currently being submitted.
 *
 * The component renders a form with an input field for file selection and a
 * submit button. The form is decorated with a dashed border and a colored
 * background that changes depending on whether a file is selected or not.
 * The component also handles drag and drop events to allow users to drag a file
 * and drop it on the form to select it.
 *
 * The component is designed to be used with the `useUploadFile` hook, which
 * provides an `onSubmit` callback that can be passed to the component.
 *
 * @example
 * import { useUploadFile } from "../hooks/useUploadFile";
 *
 * export const MyComponent = () => {
 *   const { onSubmit, isLoading } = useUploadFile();
 *
 *   return (
 *     <UploadForm onSubmit={onSubmit} isLoading={isLoading} />
 *   );
 * };
 */
export const UploadForm = ({ onSubmit, isLoading }: UploadFormProps) => {
	const [file, setFile] = useState<File | null>(null);
	const [isDragging, setIsDragging] = useState(false);
	const fileInputRef = useRef<HTMLInputElement>(null);

	const handleSubmit = (e: React.FormEvent) => {
		e.preventDefault();
		if (file) onSubmit(file);
	};

	const handleDragOver = useCallback((e: React.DragEvent) => {
		e.preventDefault();
		setIsDragging(true);
	}, []);

	const handleDragLeave = useCallback((e: React.DragEvent) => {
		e.preventDefault();
		setIsDragging(false);
	}, []);

	const handleDrop = useCallback((e: React.DragEvent) => {
		e.preventDefault();
		setIsDragging(false);

		const droppedFiles = e.dataTransfer.files;
		if (droppedFiles.length > 0) {
			const droppedFile = droppedFiles[0];
			if (
				droppedFile.type === "text/plain" ||
				droppedFile.type === "application/pdf"
			) {
				setFile(droppedFile);
			}
		}
	}, []);

	const handleFileSelect = useCallback(
		(e: React.ChangeEvent<HTMLInputElement>) => {
			const selectedFile = e.target.files?.[0] || null;
			if (selectedFile) {
				setFile(selectedFile);
			}
		},
		[]
	);

	const removeFile = useCallback(() => {
		setFile(null);
		if (fileInputRef.current) {
			fileInputRef.current.value = "";
		}
	}, []);

	const formatFileSize = (bytes: number) => {
		if (bytes === 0) return "0 Bytes";
		const k = 1024;
		const sizes = ["Bytes", "KB", "MB", "GB"];
		const i = Math.floor(Math.log(bytes) / Math.log(k));
		return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + " " + sizes[i];
	};

	return (
		<form onSubmit={handleSubmit} className="space-y-6">
			<div
				onDragOver={handleDragOver}
				onDragLeave={handleDragLeave}
				onDrop={handleDrop}
				className={`border-2 border-dashed rounded-2xl p-6 text-center transition-all duration-300 ease-snappy cursor-pointer
          ${
						isDragging
							? "border-primary-500 bg-primary-50/50"
							: file
							? "border-accent-400 bg-accent-50/30"
							: "border-neutral-300 bg-neutral-50 hover:border-primary-400 hover:bg-primary-50/30"
					}`}
				onClick={() => fileInputRef.current?.click()}
			>
				<div className="flex flex-col items-center justify-center space-y-3">
					<div
						className={`p-3 rounded-full ${
							isDragging ? "bg-primary-100" : "bg-neutral-100"
						} transition-colors duration-300`}
					>
						<FiUpload
							className={`h-6 w-6 ${
								isDragging ? "text-primary-600" : "text-neutral-600"
							}`}
						/>
					</div>

					<div className="space-y-1">
						<p className="text-lg font-medium text-neutral-700">
							{file
								? "Arquivo selecionado"
								: "Arraste e solte seu arquivo aqui"}
						</p>
						<p className="text-sm text-neutral-500">
							{file
								? "Clique para selecionar outro arquivo"
								: "ou clique para procurar em seu dispositivo"}
						</p>
						<p className="text-xs text-neutral-400 mt-2">
							Suporta: .txt, .pdf (Máx. 10MB)
						</p>
					</div>

					{file && (
						<div className="mt-4 p-3 bg-white rounded-lg border border-neutral-200 w-full max-w-md text-left">
							<div className="flex items-center justify-between">
								<div className="flex items-center gap-2">
									<FiFile className="h-4 w-4 text-primary-600" />
									<div className="flex-1 min-w-0">
										<p className="text-sm font-medium text-neutral-800 truncate">
											{file.name}
										</p>
										<p className="text-xs text-neutral-500">
											{formatFileSize(file.size)}
										</p>
									</div>
								</div>
								<button
									type="button"
									onClick={(e) => {
										e.stopPropagation();
										removeFile();
									}}
									className="p-1 text-neutral-400 hover:text-danger-500 transition-colors duration-200"
								>
									<FiX className="h-4 w-4" />
								</button>
							</div>
						</div>
					)}
				</div>

				<input
					ref={fileInputRef}
					type="file"
					onChange={handleFileSelect}
					accept=".txt,.pdf"
					className="hidden"
				/>
			</div>

			<button
				type="submit"
				disabled={isLoading || !file}
				className={`w-full py-3 px-4 rounded-xl font-medium transition-all duration-300 ease-snappy flex items-center justify-center gap-2
          ${
						isLoading || !file
							? "bg-neutral-200 text-neutral-500 cursor-not-allowed"
							: "bg-gradient-to-r from-primary-500 to-primary-700 text-white hover:from-primary-600 hover:to-primary-800 shadow-md hover:shadow-lg"
					}`}
			>
				<FiSend className="h-4 w-4" />
				Enviar Arquivo
			</button>
		</form>
	);
};
