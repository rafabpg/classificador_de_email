import { useState } from "react";

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
