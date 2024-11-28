<?php
namespace App\Http\Controllers;

use App\Models\Libro;
use Illuminate\Http\Request;

class LibroController extends Controller
{
    public function index()
    {
        return response()->json(Libro::all());
    }

    public function show($id)
    {
        $libro = Libro::find($id);
        return $libro ? response()->json($libro) : response()->json(['message' => 'Libro no encontrado'], 404);
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'nombre' => 'required|string|max:255',
            'autor' => 'required|string|max:255',
            'anio_publicacion' => 'required|integer',
        ]);
        
        $libro = Libro::create($validated);
        return response()->json($libro, 201);
    }

    public function update(Request $request, $id)
    {
        $libro = Libro::find($id);
        if ($libro) {
            $libro->update($request->only(['nombre', 'autor', 'anio_publicacion']));
            return response()->json($libro);
        }
        return response()->json(['message' => 'Libro no encontrado'], 404);
    }

    public function destroy($id)
    {
        $libro = Libro::find($id);
        if ($libro) {
            $libro->delete();
            return response()->json(['message' => 'Libro eliminado']);
        }
        return response()->json(['message' => 'Libro no encontrado'], 404);
    }
}
