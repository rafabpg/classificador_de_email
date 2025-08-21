import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Home } from "../pages/Home";
import { Not_Found } from "../pages/Not_Found";

/**
 * Component that renders the main routes of the application.
 * The routes are defined using the `react-router-dom` library.
 * The component renders a `BrowserRouter` with a `Routes` component inside it.
 * The `Routes` component renders two `Route` components:
 * - One for the root path (`"/"`), which renders the `Home` component.
 * - One for the catch-all path (`"*"`), which renders the `Not_Found` component.
 */
export const AppRoutes = () => {
	return (
		<BrowserRouter>
			<Routes>
				<Route path="/" element={<Home />} />
				<Route path="*" element={<Not_Found />} />
			</Routes>
		</BrowserRouter>
	);
};
