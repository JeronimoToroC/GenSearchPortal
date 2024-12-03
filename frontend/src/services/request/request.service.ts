import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http'
import { environment } from '@environments/environment'
import { Injectable } from '@angular/core'
import { firstValueFrom } from 'rxjs'

@Injectable({
    providedIn: 'root',
})
export class RequestService {
    private readonly baseUrl = environment.apiUrl

    constructor(private readonly http: HttpClient) {}

    get<T>(endpoint: string, params?: HttpParams, headers?: HttpHeaders): Promise<T> {
        const options = { params, headers }
        return firstValueFrom(this.http.get<T>(`${this.baseUrl}${endpoint}`, options))
    }

    post<T>(endpoint: string, body: any, headers?: HttpHeaders): Promise<T> {
        return firstValueFrom(this.http.post<T>(`${this.baseUrl}${endpoint}`, body, { headers }))
    }

    put<T>(endpoint: string, body: any, headers?: HttpHeaders): Promise<T> {
        return firstValueFrom(this.http.put<T>(`${this.baseUrl}${endpoint}`, body, { headers }))
    }

    delete<T>(endpoint: string, headers?: HttpHeaders): Promise<T> {
        return firstValueFrom(this.http.delete<T>(`${this.baseUrl}${endpoint}`, { headers }))
    }
}
