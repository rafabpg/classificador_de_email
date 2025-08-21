import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Home } from "../pages/Home";
import { Not_Found } from "../pages/Not_Found";

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
