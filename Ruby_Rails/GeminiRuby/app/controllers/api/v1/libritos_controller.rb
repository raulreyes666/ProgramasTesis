# app/controllers/api/v1/libritos_controller.rb
module Api
    module V1
      class LibritosController < ApplicationController
        before_action :set_librito, only: [:show, :update, :destroy]
  
        def index
          @libritos = Librito.all
          render json: @libritos
        end
  
        def show
          render json: @librito
        end
  
        def create
          @librito = Librito.new(librito_params)
          if @librito.save
            render json: @librito, status: :created
          else
            render json: @librito.errors, status: :unprocessable_entity
          end
        end
  
        def update
          if @librito.update(librito_params)
            render json: @librito
          else
            render json: @librito.errors, status: :unprocessable_entity
          end
        end
  
        def destroy
          @librito.destroy
          head :no_content
        end
  
        private
  
        def set_librito
          @librito = Librito.find(params[:id])
        end
  
        def librito_params
          params.require(:librito).permit(:title, :author, :year)
        end
      end
    end
  end