import { FiX } from "react-icons/fi";
import type { ResponseAnalysis } from "../IResponse";
import { useEffect } from "react";

interface ResponseDisplayProps {
  response: ResponseAnalysis | null;
  onClear?: () => void;
}

/**
 * Component to display a response from the API, with a clear button.
 *
 * Props:
 * - `response`: The response from the API to display.
 * - `onClear`: A callback to clear the response.
 *
 * The component only renders if `response` is not null.
 *
 * The component displays a container with a category and a detail.
 * The category is displayed as a rounded badge with a background color
 * depending on the category of the response.
 * The detail is displayed as a text block below the category.
 *
 * If `onClear` is provided, a clear button is displayed in the top right
 * corner of the container.
 */
export const ResponseDisplay = ({
  response,
  onClear,
}: ResponseDisplayProps) => {
  if (!response) return null;
  useEffect(()=>{
    console.log(response)
  },[])
  const categoryColor =
    response.category === "Produtivo" 
      ? "bg-primary-500" 
      : "bg-danger-500";

  return (
    <div className="mt-6 p-6 bg-surface rounded-xl shadow-soft border border-neutral-300 relative transition-all duration-300 ease-fluid hover:shadow-md">
      <div className="flex justify-between items-center mb-4">
        <div className="flex items-center gap-3">
          <span
            className={`px-3 py-1 rounded-full text-white text-sm font-semibold ${categoryColor} transition-colors duration-300`}
          >
            {response.category}
          </span>
         
        </div>
        {onClear && (
          <button
            onClick={onClear}
            className="px-3 py-1.5 text-sm bg-neutral-200 text-neutral-700 rounded-lg hover:bg-neutral-300 transition-all duration-200 ease-snappy flex items-center gap-1.5 border border-neutral-300/50 hover:border-neutral-400/50"
            aria-label="Limpar resposta"
          >
            <FiX className="h-4 w-4" />
            Limpar
          </button>
        )}
      </div>
      
      <div className="text-neutral-700 text-base leading-relaxed whitespace-pre-wrap font-normal">
        {response.details}
      </div>
      
    </div>
  );
};