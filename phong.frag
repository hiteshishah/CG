#version 150

// Phong fragment shader
//
// Contributor:  Hiteshi Shah

// INCOMING DATA

// Material properties of the teapot and quad
uniform vec4 ambient_material_color;
uniform float ambient_reflection_coefficient;
uniform vec4 diffuse_material_color;
uniform float diffuse_reflection_coefficient;
uniform vec4 specular_material_color;
uniform float specular_exponent;
uniform float specular_reflection_coefficient;

// Properties of the light source
uniform vec4 light_color;

// Properties of the ambient light
uniform vec4 ambient_light;

in vec3 vNorm;
in vec3 light;
in vec3 vPos;

void main()
{
	vec3 N = normalize(vNorm);
	vec3 L = normalize(light - vPos);
	vec3 R = normalize (reflect(-L, N));
    vec3 V = normalize (-vPos);

	// ambient
	vec4 ambient = ambient_material_color * ambient_reflection_coefficient * ambient_light;

	// diffuse
	vec4 diffuse = diffuse_material_color * diffuse_reflection_coefficient * (dot(L, N));

	// specular
	vec4 specular = specular_material_color * specular_reflection_coefficient * pow(max(0.0, dot(R, V)), specular_exponent);

	gl_FragColor = ambient + light_color * (diffuse + specular);
}
