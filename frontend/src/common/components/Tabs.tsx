import { FiUpload, FiType } from "react-icons/fi";

interface TabsProps {
	activeTab: string;
	setActiveTab: (tab: string) => void;
}

/**
 * Component to render a tabbed interface to switch between two modes of data entry:
 * uploading a file or writing text.
 *
 * Props:
 * - `activeTab`: The currently active tab, which should be either "upload" or "text".
 * - `setActiveTab`: A callback to update the active tab.
 *
 * The component renders a container with two buttons, one for each tab.
 * The active tab is highlighted with a different background color and a shadow.
 * The component does not handle any state itself, it only renders the UI based on the props.
 */
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
