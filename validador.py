from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    Organizador: int = Field(..., description="Identificador do organizador")
    Ano_Mes: str = Field(..., description="Ano e mês do registro")
    Dia_da_Semana: str = Field(..., description="Dia da semana correspondente à data")
    Tipo_Dia: str = Field(..., description="Classificação do dia: útil, feriado, etc.")
    Objetivo: str = Field(..., description="Objetivo da campanha ou ação")
    Date: str = Field(..., description="Data da entrada no formato YYYY-MM-DD")
    AdSet_name: Optional[str] = Field(None, description="Nome do conjunto de anúncios")
    Amount_spent: float = Field(
        0.0,
        ge=0,
        le=589.96,
        description="Valor gasto no anúncio (mínimo 0, máximo 589.96)"
    )
    Link_clicks: Optional[int] = Field(
        None,
        ge=1,
        le=394,
        description="Número de cliques no link (mínimo 1, máximo 394)"
    )
    Impressions: int = Field(
        ...,
        ge=0,
        le=50782,
        description="Número de impressões do anúncio (mínimo 0, máximo 50782)"
    )
    Conversions: Optional[int] = Field(
        None,
        ge=1,
        le=361,
        description="Número de conversões registradas (mínimo 1, máximo 361)"
    )
    Segmentacao: Optional[str] = Field(None, description="Segmentação usada no anúncio")
    Tipo_de_Anuncio: str = Field(..., description="Tipo do anúncio")
    Fase: str = Field(..., description="Fase da campanha")
