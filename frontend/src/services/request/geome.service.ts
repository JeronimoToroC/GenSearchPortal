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
            Output3: item.output_3,
            Output4: item.output_4,
            Output5: item.output_5,
            Output6: item.output_6,
            Output7: item.output_7,
            Output8: item.output_8,
            Output9: item.output_9,
            Output10: item.output_10,
            Output11: item.output_11,
            Output12: item.output_12,
            Output13: item.output_13,
            Output14: item.output_14,
            Output15: item.output_15,
            Output16: item.output_16,
            Output17: item.output_17,
            Output18: item.output_18,
            Output19: item.output_19,
            Output20: item.output_20,
            Output21: item.output_21,
            Output22: item.output_22,
            Output23: item.output_23,
            Output24: item.output_24,
            Output25: item.output_25,
        }))

        return {
            resultados,
            total: (response.items_por_pagina || 0) * (response.pagina_actual || 0), // Ajustar si es necesario
        }
    }
}
