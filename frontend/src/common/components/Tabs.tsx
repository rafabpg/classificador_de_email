import { FiUpload, FiType } from "react-icons/fi";

interface TabsProps {
	activeTab: string;
	setActiveTab: (tab: string) => void;
}

export const Tabs = ({ activeTab, setActiveTab }: TabsProps) => (
	<div className="flex bg-neutral-200 p-1.5 rounded-xl mb-6 shadow-soft">
		<button
			onClick={() => setActiveTab("upload")}
			className={`flex items-center justify-center gap-2 px-4 py-3 rounded-lg text-sm font-medium transition-all duration-300 ease-snappy flex-1 ${
				activeTab === "upload"
					? "bg-white text-primary-700 shadow-sm"
					: "text-neutral-600 hover:text-neutral-800"
			}`}
		>
			<FiUpload className="h-4 w-4" />
			Upload de Arquivo
		</button>

		<button
			onClick={() => setActiveTab("text")}
			className={`flex items-center justify-center gap-2 px-4 py-3 rounded-lg text-sm font-medium transition-all duration-300 ease-snappy flex-1 ${
				activeTab === "text"
					? "bg-white text-primary-700 shadow-sm"
					: "text-neutral-600 hover:text-neutral-800"
			}`}
		>
			<FiType className="h-4 w-4" />
			Digitar Texto
		</button>
	</div>
);
