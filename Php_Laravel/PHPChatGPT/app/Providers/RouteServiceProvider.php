<?php

namespace App\Providers;

use Illuminate\Support\Facades\Route;
use Illuminate\Foundation\Support\Providers\RouteServiceProvider as ServiceProvider;

class RouteServiceProvider extends ServiceProvider
{
    /**
     * El nombre de espacio de las rutas.
     *
     * @var string
     */
    protected $namespace = 'App\\Http\\Controllers';

    /**
     * Definir las rutas para la aplicación.
     *
     * @return void
     */
    public function boot()
    {
        parent::boot();

        // Rutas de la API
        Route::prefix('api') // Prefijo "api" para las rutas
             ->middleware('api') // Middleware para las rutas de API
             ->namespace($this->namespace) // Espacio de nombres para los controladores
             ->group(base_path('routes/api.php')); // Carga las rutas definidas en api.php

        // Rutas para la aplicación web
        Route::middleware('web') // Middleware para las rutas web
             ->namespace($this->namespace) // Espacio de nombres para los controladores
             ->group(base_path('routes/web.php')); // Carga las rutas definidas en web.php
    }

    /**
     * Definir los archivos de ruta del grupo "web" y "api".
     *
     * @return void
     */
    public function map()
    {
        //
    }
}
