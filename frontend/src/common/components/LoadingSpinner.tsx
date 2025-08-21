interface LoadingPulseProps {
	isVisible?: boolean;
}

/**
 * A component that displays a loading pulse animation in the center of the screen.
 *
 * @param {{ isVisible?: boolean }} props
 * @prop {boolean} [isVisible=true] Whether the component should be visible or not.
 *
 * @returns {React.ReactElement} The loading pulse animation.
 */
const LoadingPulse = ({ isVisible = true }: LoadingPulseProps) => {
	if (!isVisible) return null;

	return (
		<div className="fixed inset-0 flex items-center justify-center z-[9999] bg-neutral-100 bg-opacity-70 backdrop-blur-sm">
			<div className="flex space-x-2">
				{[0, 0.2, 0.4].map((delay, idx) => (
					<span
						key={idx}
						className="w-3 h-3 bg-primary-500 rounded-full animate-bounce"
						style={{ animationDelay: `${delay}s` }}
					></span>
				))}
			</div>
		</div>
	);
};

export default LoadingPulse;
