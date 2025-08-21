import { toast } from "react-toastify";

/**
 * Hook that returns two functions: `showSuccess` and `showError`. Each function
 * displays a toast notification with the given message and optional options.
 *
 * The default options are:
 * - position: "top-right"
 * - autoClose: 5000
 * - hideProgressBar: false
 * - closeOnClick: true
 * - pauseOnHover: true
 * - draggable: true
 * - progress: undefined
 * - theme: "colored"
 *
 * The `showSuccess` function displays a success toast notification, while the
 * `showError` function displays an error toast notification.
 */
export const useNotification = () => {
	const showSuccess = (message: string, options = {}) => {
		toast.success(message, {
			position: "top-right",
			autoClose: 5000,
			hideProgressBar: false,
			closeOnClick: true,
			pauseOnHover: true,
			draggable: true,
			progress: undefined,
			theme: "colored",
			...options,
		});
	};

	const showError = (message: string, options = {}) => {
		toast.error(message, {
			position: "top-right",
			autoClose: 5000,
			hideProgressBar: false,
			closeOnClick: true,
			pauseOnHover: true,
			draggable: true,
			progress: undefined,
			theme: "colored",
			...options,
		});
	};

	return { showSuccess, showError };
};
