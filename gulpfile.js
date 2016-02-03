var gulp = require('gulp');
var sass = require('gulp-sass');
var autoprefixer = require('gulp-autoprefixer');
var eslint = require('gulp-eslint');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');
var browserSync = require('browser-sync').create();

gulp.task('default', function() {
  gulp.watch('app/static/sass/**/*.scss', ['styles']);
});


gulp.task('serve', ['scripts-concat','styles'], function() {

    browserSync.init({
        proxy: "localhost:8080"
    });

    gulp.watch("app/static/sass/**/*.scss", ['styles']);
    gulp.watch("app/static/js/**/*.js", ['scripts-concat','lint']);
    gulp.watch("app/templates/*.html").on('change', browserSync.reload);
    gulp.watch("app/static/directives/*.html").on('change', browserSync.reload);
    browserSync.stream();
});

gulp.task('lint', function(){
	gulp.src('app/static/js/*.js')
		.pipe(browserSync.reload());
});



gulp.task('styles', function(){
	gulp.src('app/static/sass/**/*.scss')
		.pipe(sass({outputStyle:'compressed'}).on('error', sass.logError))
		.pipe(autoprefixer({
			browsers: ['last 2 versions']
		}))
		.pipe(gulp.dest('app/static/css'))
		.pipe(browserSync.stream());
});

gulp.task('production', ['scripts-concat','scripts-compress','copy-prod']);

gulp.task('copy-prod', function(){
	gulp.src(['app/**', '!app/__init__.py'])
		.pipe(gulp.dest('prod/app'));
});

gulp.task('copy-prod2', function(){
	gulp.src('venv/lib/python2.7/site-packages/**')
		.pipe(gulp.dest('prod/lib'));
});


gulp.task('scripts-concat', function(){
	gulp.src(['app/static/js/angular/**/*.js', 'app/static/js/vanilla/**/*.js'])
		.pipe(concat('main.js'))
		.pipe(gulp.dest('app/static/js'));
});

gulp.task('scripts-compress', function(){
	gulp.src('app/static/js/main.js')
		.pipe(uglify({mangle: false}))
		.pipe(rename({suffix: '.min'}))
		.pipe(gulp.dest('app/static/js'));
	gulp.src('app/static/js/welcome.js')
		.pipe(uglify({mangle: false}))
		.pipe(rename({suffix: '.min'}))
		.pipe(gulp.dest('app/static/js'));
});
