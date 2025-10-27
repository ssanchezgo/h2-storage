package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
	"regexp"
	"strings"

	"github.com/xuri/excelize/v2"
)

// ArticleData define la estructura de datos mejorada para la información extraída
type ArticleData struct {
	Archivo                 string
	Titulo                  string
	Autor                   string
	Referencia              string
	Año                     string
	Resumen                 string
	ImagenesReferencia      []string
	ConfiguracionGeometrica string
	Dimensiones             string
	CondicionesOperacion    string
	TransferenciaCalor      string
	HidrurosMetalicos       string
	Conclusiones            string
}

func extractDataFromMD(filePath string) ArticleData {
	data := ArticleData{
		Archivo: filepath.Base(filePath),
	}

	content, err := ioutil.ReadFile(filePath)
	if err != nil {
		fmt.Printf("Error reading file %s: %v\n", filePath, err)
		return data
	}

	contentStr := string(content)

	// Título (mejorado para capturar después de "Notas de Lectura:")
	titleRegex := regexp.MustCompile(`(?m)^# Notas de Lectura: (.*?)\n`)
	if match := titleRegex.FindStringSubmatch(contentStr); len(match) > 1 {
		data.Titulo = strings.TrimSpace(match[1])
	}

	// Autor (mejorado para capturar múltiples autores)
	authorRegex := regexp.MustCompile(`(?i)\*\*Autores?:\*\* \[(.*?)\]`)
	if match := authorRegex.FindStringSubmatch(contentStr); len(match) > 1 {
		data.Autor = strings.TrimSpace(match[1])
	}

	// Referencia BibTeX
	refRegex := regexp.MustCompile(`(?i)\*\*Referencia BibTeX:\*\* \x60(.*?)\x60`)
	if match := refRegex.FindStringSubmatch(contentStr); len(match) > 1 {
		data.Referencia = strings.TrimSpace(match[1])
	}

	// Año
	yearRegex := regexp.MustCompile(`(?i)\*\*Fecha de [Pp]ublicación:\*\* \[(.*?)\]`)
	if match := yearRegex.FindStringSubmatch(contentStr); len(match) > 1 {
		data.Año = strings.TrimSpace(match[1])
	}

	// Resumen (mejorado para capturar todo el contenido hasta la siguiente sección)
	abstractRegex := regexp.MustCompile(`(?is)## 1\. Resumen y Propósito del Artículo\s*(.*?)(\n## \d\.|\n---|\z)`)
	if match := abstractRegex.FindStringSubmatch(contentStr); len(match) > 1 {
		data.Resumen = strings.TrimSpace(match[1])
	}

	// Imágenes de referencia
	baseImgPath := filepath.Join("02_research/lectura_articulos/img", strings.TrimSuffix(data.Archivo, ".md"))
	if _, err := os.Stat(baseImgPath); err == nil {
		images, err := ioutil.ReadDir(baseImgPath)
		if err == nil {
			for _, img := range images {
				if !img.IsDir() {
					data.ImagenesReferencia = append(data.ImagenesReferencia,
						filepath.Join(baseImgPath, img.Name()))
				}
			}
		}
	}

	// Configuración geométrica (mejorada para capturar más detalles)
	if strings.Contains(contentStr, "Configuracion geometrica") {
		geoRegex := regexp.MustCompile(`(?is)\*\*Configuracion geometrica\*\* : (.*?)(?:\*\*|$)`)
		if match := geoRegex.FindStringSubmatch(contentStr); len(match) > 1 {
			data.ConfiguracionGeometrica = strings.TrimSpace(match[1])
		}
	}

	// Dimensiones (mejorada para capturar lista completa)
	dimRegex := regexp.MustCompile(`(?is)\*\*Dimensiones\*\* :(.*?)(?:\*\*|$)`)
	if match := dimRegex.FindStringSubmatch(contentStr); len(match) > 1 {
		data.Dimensiones = strings.TrimSpace(match[1])
	}

	// Condiciones de operación (mejorada para capturar lista completa)
	opRegex := regexp.MustCompile(`(?is)\*\*Condiciones de Operacion\*\* :(.*?)(?:\*\*|$)`)
	if match := opRegex.FindStringSubmatch(contentStr); len(match) > 1 {
		data.CondicionesOperacion = strings.TrimSpace(match[1])
	}

	// Transferencia de calor (nueva sección)
	htRegex := regexp.MustCompile(`(?is)## 5\. Tranferencia de Calor\s*(.*?)(?:\n## \d\.|\z)`)
	if match := htRegex.FindStringSubmatch(contentStr); len(match) > 1 {
		data.TransferenciaCalor = strings.TrimSpace(match[1])
	}

	// Hidruros metálicos (nueva sección)
	mhRegex := regexp.MustCompile(`(?is)## 6\. MH Hidruro Metalico\s*(.*?)(?:\n## \d\.|\z)`)
	if match := mhRegex.FindStringSubmatch(contentStr); len(match) > 1 {
		data.HidrurosMetalicos = strings.TrimSpace(match[1])
	}

	// Conclusiones (nueva sección)
	conRegex := regexp.MustCompile(`(?is)## 7\. Conclusiones y Observaciones\s*(.*?)(?:\n## \d\.|\z)`)
	if match := conRegex.FindStringSubmatch(contentStr); len(match) > 1 {
		data.Conclusiones = strings.TrimSpace(match[1])
	}

	return data
}

func processMDFiles() error {
	fmt.Println("Starting enhanced Markdown knowledge base extractor...")

	// Crear nuevo archivo Excel
	f := excelize.NewFile()
	sheetName := "Articles"
	f.SetSheetName("Sheet1", sheetName)

	// Definir encabezados mejorados
	headers := []string{
		"Archivo", "Título", "Autor(es)", "Referencia BibTeX", "Año",
		"Resumen", "Imágenes de Referencia", "Configuración Geométrica",
		"Dimensiones", "Condiciones de Operación", "Transferencia de Calor",
		"Hidruros Metálicos", "Conclusiones",
	}

	// Escribir encabezados
	for i, header := range headers {
		col, _ := excelize.ColumnNumberToName(i + 1)
		f.SetCellValue(sheetName, col+"1", header)
		// Dar formato al encabezado
		style, _ := f.NewStyle(&excelize.Style{
			Font: &excelize.Font{Bold: true},
			Fill: excelize.Fill{Type: "pattern", Color: []string{"#CCCCCC"}, Pattern: 1},
		})
		f.SetCellStyle(sheetName, col+"1", col+"1", style)
	}

	// Procesar archivos MD
	rowNum := 2
	err := filepath.Walk("02_research/lectura_articulos", func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if !info.IsDir() && strings.HasSuffix(path, ".md") && !strings.Contains(path, "plantilla") {
			fmt.Printf("-> Processing: %s\n", path)
			data := extractDataFromMD(path)

			// Preparar los valores para las celdas
			values := []interface{}{
				data.Archivo,
				data.Titulo,
				data.Autor,
				data.Referencia,
				data.Año,
				data.Resumen,
				strings.Join(data.ImagenesReferencia, "\n"),
				data.ConfiguracionGeometrica,
				data.Dimensiones,
				data.CondicionesOperacion,
				data.TransferenciaCalor,
				data.HidrurosMetalicos,
				data.Conclusiones,
			}

			// Escribir valores
			for i, value := range values {
				col, _ := excelize.ColumnNumberToName(i + 1)
				f.SetCellValue(sheetName, fmt.Sprintf("%s%d", col, rowNum), value)
			}
			rowNum++
		}
		return nil
	})

	if err != nil {
		return fmt.Errorf("error processing files: %v", err)
	}

	// Ajustar ancho de columnas y formato
	for i := range headers {
		col, _ := excelize.ColumnNumberToName(i + 1)
		f.SetColWidth(sheetName, col, col, 40)
	}

	// Aplicar formato de texto envuelto a todas las celdas
	style, _ := f.NewStyle(&excelize.Style{
		Alignment: &excelize.Alignment{WrapText: true, Vertical: "top"},
	})
	lastCol, _ := excelize.ColumnNumberToName(len(headers))
	f.SetCellStyle(sheetName, "A2", fmt.Sprintf("%s%d", lastCol, rowNum-1), style)

	// Guardar archivo Excel
	return f.SaveAs("base_de_conocimiento_H2_storage_mejorada.xlsx")
}

func main() {
	if err := processMDFiles(); err != nil {
		log.Fatalf("Error: %v", err)
	}
	fmt.Println("Proceso completado. Archivo generado: base_de_conocimiento_H2_storage_mejorada.xlsx")
}
