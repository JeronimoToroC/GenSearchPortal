import axios, { AxiosInstance } from 'axios'
import { environment } from '@environments/environment'

export class AxiosService {
    private readonly instance: AxiosInstance

    constructor() {
        this.instance = axios.create({
            baseURL: environment.apiUrl,
            timeout: 5000,
        })

        this.instance.interceptors.response.use(
            (response) => response,
            (error) => {
                console.error('Axios Error:', error)

                const rejectionError = error instanceof Error ? error : new Error(error.message || 'Unknown error')
                return Promise.reject(rejectionError)
            }
        )
    }

    async get<T>(endpoint: string, params?: any): Promise<T> {
        const response = await this.instance.get<T>(endpoint, { params })
        return response.data
    }

    async post<T>(endpoint: string, body: any): Promise<T> {
        const response = await this.instance.post<T>(endpoint, body)
        return response.data
    }

    async put<T>(endpoint: string, body: any): Promise<T> {
        const response = await this.instance.put<T>(endpoint, body)
        return response.data
    }

    async delete<T>(endpoint: string): Promise<T> {
        const response = await this.instance.delete<T>(endpoint)
        return response.data
    }
}
