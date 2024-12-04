import { Injectable } from '@angular/core'
import { AxiosService } from './axios.service'

@Injectable({
    providedIn: 'root',
})
export class RequestService {
    private readonly axiosService: AxiosService

    constructor() {
        this.axiosService = new AxiosService()
    }

    get<T>(endpoint: string, params?: any): Promise<T> {
        return this.axiosService.get(endpoint, params)
    }

    post<T>(endpoint: string, body: any): Promise<T> {
        return this.axiosService.post(endpoint, body)
    }

    put<T>(endpoint: string, body: any): Promise<T> {
        return this.axiosService.put(endpoint, body)
    }

    delete<T>(endpoint: string): Promise<T> {
        return this.axiosService.delete(endpoint)
    }
}
