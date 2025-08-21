import { useState } from "react";
import { FiSend, FiType } from "react-icons/fi";

interface TextFormProps {
	onSubmit: (text: string) => void;
	isLoading: boolean;
}

export const TextForm = ({ onSubmit, isLoading }: TextFormProps) => {
	const [text, setText] = useState("");

	const handleSubmit = (e: React.FormEvent) => {
		e.preventDefault();
		if (text.trim()) onSubmit(text);
	};

	return (
		<form onSubmit={handleSubmit} className="space-y-5">
			<div className="relative">
				<div className="flex items-center gap-2 mb-3">
					<FiType className="h-5 w-5 text-primary-600" />
					<label
						htmlFor="text-input"
						className="text-sm font-medium text-neutral-700"
					>
						Digite seu texto para análise
					</label>
				</div>

				<textarea
					id="text-input"
					value={text}
					onChange={(e) => setText(e.target.value)}
					placeholder="Cole ou digite o conteúdo do email aqui..."
					rows={6}
					className="w-full p-4 border border-neutral-300 rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-primary-300 focus:outline-none transition-all duration-300 ease-snappy text-neutral-700 placeholder-neutral-400 resize-none shadow-sm hover:shadow-md"
					disabled={isLoading}
				/>

				<div className="flex justify-between items-center mt-2">
					<span
						className={`text-xs ${
							text.length > 0 ? "text-neutral-500" : "text-neutral-400"
						}`}
					>
						{text.length} caracteres
					</span>
					{text.length > 0 && (
						<button
							type="button"
							onClick={() => setText("")}
							className="text-xs text-neutral-500 hover:text-danger-500 transition-colors duration-200"
						>
							Limpar
						</button>
					)}
				</div>
			</div>

			<button
				type="submit"
				disabled={isLoading || !text.trim()}
				className={`w-full py-3 px-4 rounded-xl font-medium transition-all duration-300 ease-snappy flex items-center justify-center gap-2
          ${
						isLoading || !text.trim()
							? "bg-neutral-200 text-neutral-500 cursor-not-allowed"
							: "bg-gradient-to-r from-accent-400 to-accent-600 text-white hover:from-accent-500 hover:to-accent-700 shadow-md hover:shadow-lg transform hover:-translate-y-0.5"
					}`}
			>
				<FiSend className="h-4 w-4" />
				Analisar Texto
			</button>

			<div className="text-xs text-neutral-400 text-center pt-2">
				<p>O texto será analisado e classificado automaticamente</p>
			</div>
		</form>
	);
};
