import { Injectable } from '@angular/core'
import { RequestService } from './request.service'
import { GenModel } from '@models/gen.model'

@Injectable({
    providedIn: 'root',
})
export class GenomeService {
    constructor(private readonly requestService: RequestService) {}

    async searchGenomes(
        coincidence: string,
        page: number = 1,
        itemsPerPage: number = 10
    ): Promise<{ resultados: GenModel[]; total: number }> {
        const response: any = await this.requestService.get('/genomes', {
            coincidence,
            page,
            items_per_page: itemsPerPage,
        })

        // Mapear las propiedades del backend al modelo GenModel
        const resultados = response.resultados.map((item: any) => ({
            Chrom: item.chrom,
            Pos: item.pos,
            Id: item.id || '', // Asignar valor predeterminado si falta
            Ref: item.ref,
            Alt: item.alt,
            Qual: item.qual || '',
            Filter: item.filter,
            Info: item.info,
            Format: item.format,
            Output1: item.output_1,
            Output2: item.output_2,
        }))

        return {
            resultados,
            total: (response.items_por_pagina || 0) * (response.pagina_actual || 0), // Ajustar si es necesario
        }
    }
}
