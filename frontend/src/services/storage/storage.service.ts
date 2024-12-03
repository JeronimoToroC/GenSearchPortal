import { Injectable } from '@angular/core'

@Injectable({
    providedIn: 'root'
})
export class StorageService {
    setItem(key: string, value: unknown): void {
        try {
            const serializedValue = JSON.stringify(value)
            localStorage.setItem(key, serializedValue)
        } catch (error) {
            console.error('Error al guardar en localStorage:', error)
        }
    }

    getItem<T>(key: string): T | null {
        try {
            const item = localStorage.getItem(key)
            return item ? JSON.parse(item) : null
        } catch (error) {
            console.error('Error al obtener de localStorage:', error)
            return null
        }
    }

    removeItem(key: string): void {
        try {
            localStorage.removeItem(key)
        } catch (error) {
            console.error('Error al eliminar de localStorage:', error)
        }
    }

    clear(): void {
        try {
            localStorage.clear()
        } catch (error) {
            console.error('Error al limpiar localStorage:', error)
        }
    }
} 