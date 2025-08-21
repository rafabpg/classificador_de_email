import api from "../config/api";

export interface UploadResponse {
	success: boolean;
	message?: string;
	data?: any;
}

export function apiFiles() {
	async function uploadFile(file: File): Promise<UploadResponse> {
		const formData = new FormData();
		formData.append("file", file);

		const response = await api.post("/analysis", formData, {
			headers: { "Content-Type": "multipart/form-data" },
		});

		return response.data;
	}

	async function uploadText(text: string): Promise<UploadResponse> {
		const formData = new FormData();
		formData.append("text", text);

		const response = await api.post("/analysis", formData, {
			headers: { "Content-Type": "multipart/form-data" },
		});

		return response.data;
	}

	return { uploadFile, uploadText };
}
