var gulp           = require('gulp'),
		sass           = require('gulp-sass'),
		browserSync    = require('browser-sync'),
		autoprefixer   = require('gulp-autoprefixer'),
		notify         = require("gulp-notify");


// Пользовательские скрипты проекта

gulp.task('sass', function() {
	return gulp.src('todo_app/index_page/static/sass/**/**/*.sass')
	.pipe(sass({outputStyle: 'expand'}).on("error", notify.onError()))
	//.pipe(rename({suffix: '.min', prefix : ''}))
	.pipe(autoprefixer(['last 15 versions']))
	//.pipe(cleanCSS()) // Опционально, закомментировать при отладке
	.pipe(gulp.dest('todo_app/index_page/static/css'))
	.pipe(browserSync.reload({stream: true}));
});

gulp.task('watch', ['sass'], function() {
	gulp.watch('todo_app/index_page/static/sass/**/**/*.sass', ['sass']);
});

gulp.task('default', ['watch']);
