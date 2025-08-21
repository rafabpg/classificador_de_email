import { useState } from "react";

/**
 * Hook to control a pulsing state.
 *
 * This hook is used to control a pulsing state. It returns an object with
 * three properties: `isPulsing`, `startPulse`, and `stopPulse`. The
 * `isPulsing` property is a boolean that indicates whether the pulsing is
 * active. The `startPulse` and `stopPulse` functions can be used to
 * activate or deactivate the pulsing state.
 *
 * @returns {Object} An object with three properties: `isPulsing`, `startPulse`, and `stopPulse`.
 */
const usePulse = () => {
	const [isPulsing, setIsPulsing] = useState(false);

	const startPulse = () => {
		setIsPulsing(true);
	};

	const stopPulse = () => {
		setIsPulsing(false);
	};

	return { isPulsing, startPulse, stopPulse };
};

export default usePulse;
