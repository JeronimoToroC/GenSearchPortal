import { Component, OnInit } from '@angular/core'
import { CommonModule } from '@angular/common'
import { FormsModule } from '@angular/forms'
import { ButtonComponent } from '@common-components/Button/button.component'
import { LogoutButtonComponent } from '@common-components/LogoutButton/logout-button.component'
import { GenModel } from '@models/gen.model'
import { GenomeService } from '@services/request/geome.service'

@Component({
    selector: 'app-home',
    standalone: true,
    imports: [ButtonComponent, CommonModule, FormsModule, LogoutButtonComponent],
    templateUrl: './home.component.html',
    styleUrls: ['./home.component.scss'],
})
export class HomeComponent implements OnInit {
    genes: GenModel[] = []
    currentPage = 1
    itemsPerPage = 6
    isLastPage = false
    searchInput = ''
    noResults = false
    isLoading = false // Estado de carga

    outputs: string[] = Array.from({ length: 25 }, (_, i) => `Salida ${i + 1}`)

    constructor(private readonly genomeService: GenomeService) {}

    ngOnInit(): void {
        this.loadGenomes()
    }

    /**
     * Carga los datos desde el backend con un timeout de 5 segundos
     */
    async loadGenomes(): Promise<void> {
        this.isLoading = true // Iniciar el estado de carga
        this.genes = [] // Limpiar la tabla antes de la consulta
        this.noResults = false

        // Crear una promesa para el timeout
        const timeout = new Promise<never>((_, reject) => {
            setTimeout(() => reject(new Error('Timeout: La solicitud tardó más de 5 segundos')), 4000)
        })

        try {
            // Forzar a TypeScript a reconocer el tipo de respuesta
            const response = (await Promise.race([
                this.genomeService.searchGenomes(this.searchInput, this.currentPage, this.itemsPerPage),
                timeout,
            ])) as { resultados: GenModel[] }

            if (response && response.resultados) {
                this.genes = response.resultados
                this.noResults = response.resultados.length === 0
                this.isLastPage = response.resultados.length < this.itemsPerPage
            } else {
                this.noResults = true
            }
        } catch (error) {
            console.error('Error loading genomes:', (error as Error).message) // Type assertion para el error
            this.noResults = true
            this.genes = []
        } finally {
            this.isLoading = false // Finalizar el estado de carga
        }
    }

    get paginatedGenes(): GenModel[] {
        return this.genes
    }

    /**
     * Acciones del botón de búsqueda:
     * - Resetea la tabla.
     * - Reinicia paginación.
     * - Realiza la consulta.
     */
    onSearch(): void {
        this.currentPage = 1
        this.isLastPage = false
        this.noResults = false
        this.genes = [] // Limpiar los datos
        this.loadGenomes()
    }

    /**
     * Manejo de paginación
     */
    onPageChange(page: number): void {
        if (page > 0 && !this.isLastPage) {
            this.currentPage = page
            this.loadGenomes()
        }
    }

    /**
     * Filtra dinámicamente las salidas válidas del modelo
     */
    getOutputValues(gen: Partial<GenModel>): string[] {
        const outputs: string[] = []
        for (let i = 1; i <= 25; i++) {
            const outputKey = `Output${i}`
            if (gen[outputKey as keyof GenModel]) {
                outputs.push(gen[outputKey as keyof GenModel] as string)
            }
        }
        return outputs
    }
}
