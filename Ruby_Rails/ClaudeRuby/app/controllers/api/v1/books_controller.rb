# app/controllers/api/v1/books_controller.rb
module Api
    module V1
      class BooksController < ApplicationController
        before_action :set_book, only: [:show, :update, :destroy]
  
        # GET /api/v1/books
        def index
          @books = Book.all
          render json: @books
        end
  
        # GET /api/v1/books/1
        def show
          render json: @book
        end
  
        # POST /api/v1/books
        def create
          @book = Book.new(book_params)
  
          if @book.save
            render json: @book, status: :created
          else
            render json: @book.errors, status: :unprocessable_entity
          end
        end
  
        # PATCH/PUT /api/v1/books/1
        def update
          if @book.update(book_params)
            render json: @book
          else
            render json: @book.errors, status: :unprocessable_entity
          end
        end
  
        # DELETE /api/v1/books/1
        def destroy
          @book.destroy
          head :no_content
        end
  
        private
  
        def set_book
          @book = Book.find(params[:id])
        end
  
        def book_params
          params.require(:book).permit(:title, :author, :year)
        end
      end
    end
  end