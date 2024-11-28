class LibrosController < ApplicationController
    # Listar todos los libros
    def index
      @libros = Libro.all
      render json: @libros
    end
  
    # Mostrar un libro específico
    def show
      @libro = Libro.find(params[:id])
      render json: @libro
    end
  
    # Crear un nuevo libro
    def create
      @libro = Libro.new(libro_params)
      if @libro.save
        render json: @libro, status: :created
      else
        render json: @libro.errors, status: :unprocessable_entity
      end
    end
  
    # Actualizar un libro existente
    def update
      @libro = Libro.find(params[:id])
      if @libro.update(libro_params)
        render json: @libro
      else
        render json: @libro.errors, status: :unprocessable_entity
      end
    end
  
    # Eliminar un libro
    def destroy
      @libro = Libro.find(params[:id])
      @libro.destroy
      head :no_content
    end
  
    private
  
    # Strong parameters
    def libro_params
      params.require(:libro).permit(:titulo, :autor, :anio_publicacion)
    end
  end
  