<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Jueguito de Clay</title>
    <style>
        body { margin: 0; overflow: hidden; background: black; font-family: monospace; }
        canvas { display: block; }
        #ui { position: absolute; top: 20px; left: 20px; color: white; font-size: 24px; }
    </style>
</head>
<body>
    <div id="ui">Puntos: 0</div>
    <canvas id="gameCanvas"></canvas>

    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        const ui = document.getElementById('ui');

        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        let puntuacion = 0;
        let velocidad = 5;
        let gameOver = false;

        const jugador = {
            x: canvas.width / 2 - 50,
            y: canvas.height - 150,
            tamano: 80,
            color: 'blue'
        };

        const enemigo = {
            x: Math.random() * (canvas.width - 80),
            y: 0,
            tamano: 80,
            color: 'red'
        };

        // Control táctil
        window.addEventListener('touchmove', (e) => {
            let touchX = e.touches[0].clientX;
            jugador.x = touchX - jugador.tamano / 2;
        });

        function actualizar() {
            if (gameOver) return;

            enemigo.y += velocidad;

            if (enemigo.y > canvas.height) {
                enemigo.y = -80;
                enemigo.x = Math.random() * (canvas.width - enemigo.tamano);
                puntuacion++;
                velocidad += 0.2;
                ui.innerText = `Puntos: ${puntuacion}`;
            }

            // Colisión
            if (jugador.x < enemigo.x + enemigo.tamano &&
                jugador.x + jugador.tamano > enemigo.x &&
                jugador.y < enemigo.y + enemigo.tamano &&
                jugador.y + jugador.tamano > enemigo.y) {
                gameOver = true;
                alert("Juego terminado. Puntos: " + puntuacion);
                location.reload();
            }
        }

        function dibujar() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // Jugador
            ctx.fillStyle = jugador.color;
            ctx.fillRect(jugador.x, jugador.y, jugador.tamano, jugador.tamano);

            // Enemigo
            ctx.fillStyle = enemigo.color;
            ctx.fillRect(enemigo.x, enemigo.y, enemigo.tamano, enemigo.tamano);

            actualizar();
            requestAnimationFrame(dibujar);
        }

        dibujar();
    </script>
</body>
</html>
