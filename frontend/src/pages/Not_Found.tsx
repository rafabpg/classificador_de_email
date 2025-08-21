import { Link } from "react-router-dom";

export const Not_Found = () => {
	return (
		<div className="min-h-screen flex flex-col items-center justify-center bg-background font-sans text-neutral-700 px-4">
			<div className="bg-surface shadow-soft rounded-xl p-10 text-center">
				<div className="text-6xl text-primary-500 mb-4">
					<i className="fas fa-envelope-open-text"></i>
				</div>

				<h1 className="text-5xl font-bold text-neutral-900 mb-2">404</h1>
				<p className="text-lg text-neutral-500 mb-6">
					Oops! Página não encontrada.
				</p>

				<Link
					to="/"
					className="inline-flex items-center gap-2 bg-primary-500 text-white px-6 py-3 rounded-lg font-semibold shadow-soft hover:bg-primary-700 transition ease-snappy"
				>
					<i className="fas fa-home"></i> Voltar para Início
				</Link>
			</div>
		</div>
	);
};
