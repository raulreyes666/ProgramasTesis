Rails.application.routes.draw do
  # Rutas CRUD para el modelo Libro
  resources :libros, only: [:index, :show, :create, :update, :destroy]
end
