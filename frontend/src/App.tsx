import { AppRoutes } from "./routes/routes";
import { queryClient } from "./config/queryClient";
import { QueryClientProvider } from "@tanstack/react-query";
import { ToastContainer } from "react-toastify";

/**
 * The root component of the app.
 *
 * It wraps the {@link AppRoutes} component with the {@link QueryClientProvider}
 * component, which provides the {@link QueryClient} instance to all React Query
 * hooks in the app. It also renders the {@link ToastContainer} component, which
 * displays any React Query errors as toast notifications.
 */
function App() {
	return (
		<QueryClientProvider client={queryClient}>
			<AppRoutes />
			<ToastContainer />
		</QueryClientProvider>
	);
}

export default App;
