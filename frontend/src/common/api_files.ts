import api from "../config/api";


/**
 * apiFiles returns an object with two functions, uploadFile and uploadText.
 *
 * Both functions make a POST request to the "/analysis" endpoint with the provided
 * file or text. The response from the server is returned as the result of the
 * function call.
 *
 * @returns {{ uploadFile: (file: File) => Promise<any>, uploadText: (text: string) => Promise<any> }}
 */
export function apiFiles() {
	async function uploadFile(file: File){
		const formData = new FormData();
		formData.append("file", file);

		const response = await api.post("/analysis", formData, {
			headers: { "Content-Type": "multipart/form-data" },
		});

		return response.data;
	}

	async function uploadText(text: string) {
		const formData = new FormData();
		formData.append("text", text);

		const response = await api.post("/analysis", formData, {
			headers: { "Content-Type": "multipart/form-data" },
		});

		return response.data;
	}

	return { uploadFile, uploadText };
}
